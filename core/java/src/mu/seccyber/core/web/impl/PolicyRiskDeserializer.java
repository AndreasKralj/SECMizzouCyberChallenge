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
public class PolicyRiskDeserializer extends JsonDeserializer<PolicyRisk> implements CoreServerConstants {
    @Override
    public PolicyRisk deserialize(JsonParser jp, DeserializationContext dC) throws IOException, JsonProcessingException {
        double riskLvl = -1.0;

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
                case RISK_LVL:
                    riskLvl = jp.getDoubleValue();
                default:
                    break;
            }
        }

        if (riskLvl >=0) {
            return new PolicyRisk(riskLvl);
        }
        else
            throw new IOException("wrong Action parameters");
    }
}
