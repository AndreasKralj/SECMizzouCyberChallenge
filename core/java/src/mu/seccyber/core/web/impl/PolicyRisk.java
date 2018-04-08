package mu.seccyber.core.web.impl;

import com.fasterxml.jackson.databind.annotation.JsonDeserialize;

/**
 * Created by dmitriichemodanov on 4/8/18.
 */

@JsonDeserialize(using = PolicyRiskDeserializer.class)
public class PolicyRisk {
    private double risk_lvl = 0.0;

    public PolicyRisk(double riskLvl)
    {
        this.risk_lvl = riskLvl;
    }

    public double getRiskLvl()
    {
        return risk_lvl;
    }
}
