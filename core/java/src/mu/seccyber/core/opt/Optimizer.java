package mu.seccyber.core.opt;

import ilog.concert.IloException;
import ilog.concert.IloNumExpr;
import ilog.concert.IloNumVar;
import ilog.concert.IloRange;
import ilog.cplex.IloCplex;

/**
 * Created by dmitriichemodanov on 4/8/18.
 */
public class Optimizer {
    public int[] composeActions(int acts_num, double[] risks, double[] exec_times, double risk_lvl)
    {
        int[] solution = new int[acts_num];

        try {
            IloCplex cplex = new IloCplex();
            IloNumVar[][] var = new IloNumVar[1][];
            IloRange[][] rng = new IloRange[1][];
            //construct IP and solve
            constructIP(cplex, var, rng, acts_num, risks, exec_times, risk_lvl);
            cplex.setOut(null);
            //cplex.setParam(IloCplex.Param.TimeLimit, 120);
            if (cplex.solve())
            {
               double[] res = cplex.getValues(var[0]);
               for (int j = 0; j < var[0].length; j++) {
                   solution[j] = (int) Math.round(res[j]);
               }
            }else throw  new RuntimeException("No feasible composition found.");
            cplex.end();
        } catch (IloException e) {
            throw new RuntimeException("Concert exception caught '" + e + "' caught");
        }

        return solution;
    }

    private void constructIP(IloCplex model, IloNumVar[][] var, IloRange[][] rng,
                             int acts_num, double[] risks, double[] exec_times, double risk_lvl) throws IloException {
        //add vars
        IloNumVar[] f = model.boolVarArray(acts_num);
        var[0] = f;
        //add obj
        model.addMinimize(model.scalProd(f, exec_times));
        //add cnstrs
        rng[0] = new IloRange[1];
        IloNumExpr[] act_risks = new IloNumExpr[acts_num];
        for (int i = 0; i < act_risks.length; i++)
            act_risks[i] = model.prod(Math.log(risks[i]), var[0][i]);
        rng[0][0] = model.addLe(model.sum(act_risks), Math.log(risk_lvl));
    }
}
