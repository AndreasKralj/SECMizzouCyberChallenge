package mu.seccyber.core.web.impl;

import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonSerializer;
import com.fasterxml.jackson.databind.SerializerProvider;
import mu.seccyber.core.CoreServerConstants;

import java.io.IOException;

/**
 * Created by chemo_000 on 4/27/2015.
 */
public class ActionSerializer extends JsonSerializer<Action> implements CoreServerConstants
{
    @Override
    public void serialize(Action a, JsonGenerator jgen, SerializerProvider arg) throws IOException, JsonProcessingException
    {
        jgen.writeStartObject();
        jgen.writeStringField(NAME, a.getName());
        jgen.writeNumberField(RISK, a.getRisk());
        jgen.writeNumberField(EXEC_TIME, a.getExecTime());
        jgen.writeBooleanField(APPLY, a.apply());
        jgen.writeEndObject();
    }
}
