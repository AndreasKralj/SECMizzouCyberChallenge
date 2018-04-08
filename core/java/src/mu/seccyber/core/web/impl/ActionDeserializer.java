package mu.seccyber.core.web.impl;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.JsonToken;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.JsonDeserializer;
import mu.seccyber.core.CoreServerConstants;

import java.io.IOException;

/**
 * Created by chemo_000 on 4/27/2015.
 */
public class ActionDeserializer extends JsonDeserializer<Action> implements CoreServerConstants {

    @Override
    public Action deserialize(JsonParser jp, DeserializationContext dC) throws IOException, JsonProcessingException {
        String name = null;
        double risk = -1.0;
        double exec_time = -1.0;
        boolean apply = false;

        if (jp.getCurrentToken() != JsonToken.START_OBJECT) {
            throw new IOException("Expected START_OBJECT");
        }

        while (jp.nextToken() != JsonToken.END_OBJECT) {
            if (jp.getCurrentToken() != JsonToken.FIELD_NAME) {
                throw new IOException("Expected FIELD_NAME");
            }

            String n = jp.getCurrentName();
            jp.nextToken();
            if (jp.getText().equals("")) {
                continue;
            }

            switch (n) {
                case NAME:
                    name = jp.getText();
                    break;
                case RISK:
                    risk = jp.getDoubleValue();
                    break;
                case EXEC_TIME:
                    exec_time = jp.getDoubleValue();
                    break;
                case APPLY:
                    apply = jp.getBooleanValue();
                    break;
                default:
                    break;
            }
        }

        if (name != null && risk >=0 && exec_time >= 0)
            return  new Action(name, risk, exec_time, apply);
        else
            throw new IOException("wrong Action parameters");
    }
}
