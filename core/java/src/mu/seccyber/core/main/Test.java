package mu.seccyber.core.main;

import mu.seccyber.core.opt.Optimizer;

import java.util.Arrays;

/**
 * Created by dmitriichemodanov on 4/8/18.
 */
public class Test {
    public static void main(String[] args) {
        // write your code here
        int acts_num = 5;

        double[] risks = {0.01, 0.05, 0.001, 0.1, 0.03};
        double[] exec_times = {5, 2, 10, 2, 1};

        double[] riskLvls = {0.000001, 0.0001, 0.001, 0.005, 0.01, 0.05};

        for (double riskLvl : riskLvls) {
            System.out.println("=======================================");
            System.out.println("+ Risk lvl req.=" + (riskLvl) * 100 + "%..");
            long start = System.currentTimeMillis();
            int[] acts = new Optimizer().composeActions(acts_num, risks, exec_times, riskLvl);
            System.out.println("+ Sec. acts are composed in " +
                    Double.valueOf(System.currentTimeMillis() - start) / 1000 + " sec.. ");
            System.out.println("+ Actual risk lvl=" + compute_risk(acts, risks)*100 + "%..");
            System.out.println("+ Action chosen = " + Arrays.toString(acts));
            System.out.println("+ Total exec time = " + compute_total_exec_time(acts, exec_times));
            System.out.println("=======================================");
            System.out.println();
        }
    }

    private static double compute_total_exec_time(int[] acts, double[] exec_times)
    {
        double exec_time = 0;
        for(int i=0; i< acts.length; i++)
            if(acts[i] == 1)
                exec_time += exec_times[i];
        return exec_time;
    }

    private static double compute_risk(int[] acts, double[] risks)
    {
        double log_risk = 0;
        for(int i=0; i< acts.length; i++)
            if(acts[i] == 1)
                log_risk += Math.log(risks[i]);
        return Math.exp(log_risk);
    }
}
