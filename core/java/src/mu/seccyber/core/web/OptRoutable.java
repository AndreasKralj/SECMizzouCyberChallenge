package mu.seccyber.core.web;

import com.fasterxml.jackson.databind.JsonDeserializer;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.deser.BeanDeserializerModifier;
import com.fasterxml.jackson.databind.module.SimpleModule;
import mu.seccyber.core.opt.Optimizer;
import mu.seccyber.core.policy.PolicyHandler;
import mu.seccyber.core.web.impl.Action;
import org.restlet.resource.Post;
import org.restlet.resource.ServerResource;

import java.io.IOException;
import java.util.List;

/**
 * Created by dmitriichemodanov on 4/8/18.
 */
public class OptRoutable extends ServerResource {
    private static  Optimizer opt = new Optimizer();

    @Post("json")
    public String composeActions(String json) {
            try {
                List<Action> actions = jsonToActions(json);
                //Compose SC
                int[] actionsToApply = composeActionsInt(actions);
                for (int i=0; i< actionsToApply.length; i++)
                            actions.get(i).setApply(actionsToApply[i] == 1);
                return actionToJson(actions);
            } catch (Exception ex) {
                ex.printStackTrace();
                return ("{\"ERROR\" : \"exception during security action composition: " + ex.getMessage() + "\"}");
            }
    }

    private int[] composeActionsInt(List<Action> acts) {
        double[] risks = new double[acts.size()];
        double[] exec_times = new double[acts.size()];
        for(int i=0; i<acts.size(); i++) {
            risks[i] = acts.get(i).getRisk();
            exec_times[i] = acts.get(i).getExecTime();
        }
        return opt.composeActions(acts.size(), risks, exec_times,
                PolicyHandler.getInstance().getRiskLvl());
    }

    public static List<Action> jsonToActions(String json) throws IOException {
        /*
        SimpleModule module = new SimpleModule();
        module.setDeserializerModifier(new BeanDeserializerModifier() {
            @Override public JsonDeserializer<?> modifyDeserializer(
                    DeserializationConfig config, BeanDescription beanDesc, JsonDeserializer<?> deserializer) {
                if (beanDesc.getBeanClass() == YourClass.class) {
                    return new YourClassDeserializer(deserializer);
                }

                return deserializer;
            }});

        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.registerModule(module);
        objectMapper.readValue(json, classType);
        */
        System.out.println("Next JSON obtained: " + json);
        ObjectMapper mapper = new ObjectMapper();
        //deserialize JSON objects
        return mapper.readValue(json,
                mapper.getTypeFactory().constructCollectionType(List.class, Action.class));
    }

    public static String actionToJson(List<Action> acts) throws IOException {
        return new ObjectMapper().writeValueAsString(acts);
    }

}
