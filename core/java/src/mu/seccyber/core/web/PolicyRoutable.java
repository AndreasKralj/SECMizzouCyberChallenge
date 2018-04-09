package mu.seccyber.core.web;

import com.fasterxml.jackson.databind.ObjectMapper;
import mu.seccyber.core.CoreServerConstants;
import mu.seccyber.core.policy.PolicyHandler;
import mu.seccyber.core.web.impl.PolicyRisk;

import org.restlet.resource.Post;
import org.restlet.resource.ServerResource;

import java.io.IOException;

/**
 * Created by dmitriichemodanov on 4/8/18.
 */
public class PolicyRoutable extends ServerResource implements CoreServerConstants {

    @Post("json")
    public String updatePolicy(String json) {
        ObjectMapper mapper = new ObjectMapper();
        //deserialize JSON objects
        try {
            PolicyRisk p = mapper.readValue(json, PolicyRisk.class);
            PolicyHandler.getInstance().setRiskLvl(p.getRiskLvl());
        }catch (IOException ex)
        {
            ex.printStackTrace();
            return ("{\"ERROR\" : \"exception during the policy risk update: " + ex.getMessage() + "\"}");
        }

        return ("{\""+ RISK_LVL +"\" : " + PolicyHandler.getInstance().getRiskLvl() + "}");
    }
}
