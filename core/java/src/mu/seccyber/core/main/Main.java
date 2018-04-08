package mu.seccyber.core.main;

import mu.seccyber.core.CoreServerConstants;
import mu.seccyber.core.web.CoreRestApp;
import org.restlet.Component;
import org.restlet.data.Protocol;

public class Main implements CoreServerConstants{
    public static void main(String[] args) throws Exception {
            final Component component = new Component();
            component.getServers().add(Protocol.HTTP, SERVER_PORT);
            component.getClients().add(Protocol.CLAP);
            CoreRestApp app = new CoreRestApp();
            component.getDefaultHost().attach(app);
            component.start();
    }
}
