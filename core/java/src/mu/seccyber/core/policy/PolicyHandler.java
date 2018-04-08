package mu.seccyber.core.policy;

import java.util.concurrent.ConcurrentHashMap;

/**
 * Created by dmitriichemodanov on 4/8/18.
 */
public class PolicyHandler {
    private double riskLvl = 1.0;

    private static PolicyHandler instance = new PolicyHandler();

    public static PolicyHandler getInstance() {
        return instance;
    }

    private PolicyHandler() {
        this.riskLvl = 1.0;
    }

    public double getRiskLvl(){return this.riskLvl;}

    public void setRiskLvl(double riskLvl)
    {
        this.riskLvl = riskLvl;
    }
}
