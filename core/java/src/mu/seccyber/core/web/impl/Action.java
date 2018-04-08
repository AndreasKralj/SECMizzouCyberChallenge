package mu.seccyber.core.web.impl;

import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

/**
 * Created by dmitriichemodanov on 4/8/18.
 */
@JsonSerialize(using = ActionSerializer.class)
@JsonDeserialize(using = ActionDeserializer.class)
public class Action {
    private String name = "";
    private double risk = 0.0;
    private double exec_time = 0.0;
    private boolean apply = false;

    Action(String name, double risk, double exec_time, boolean apply)
    {
        this.name = name;
        this.risk = risk;
        this.exec_time = exec_time;
        this.apply = apply;
    }

    String getName()
    {
        return this.name;
    }

    public double getRisk()
    {
        return this.risk;
    }

    public double getExecTime()
    {
        return this.exec_time;
    }

    boolean apply()
    {
        return this.apply;
    }

    public void setApply(boolean apply)
    {
        this.apply = apply;
    }
}
