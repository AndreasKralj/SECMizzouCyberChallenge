package mu.seccyber.core.web;

import org.restlet.*;
import org.restlet.data.Reference;
//import org.restlet.resource.ServerResource;
//import org.restlet.routing.Filter;
import org.restlet.routing.Filter;
import org.restlet.routing.Router;
import org.restlet.routing.Template;

/**
 * Created by dmitriichemodanov on 4/8/18.
 */
public class CoreRestApp extends Application {

    public synchronized Restlet createInboundRoot() {
        Router baseRouter = new Router(getContext());
        baseRouter.setDefaultMatchingMode(Template.MODE_STARTS_WITH);
        baseRouter.attach("/core/compose_actions", OptRoutable.class);
        baseRouter.attach("/core/update_policy", PolicyRoutable.class);

        Filter slashFilter = new Filter() {
            @Override
            protected int beforeHandle(Request request, Response response) {
                Reference ref = request.getResourceRef();
                String originalPath = ref.getPath();
                if (originalPath.contains("//"))
                {
                    String newPath = originalPath.replaceAll("/+", "/");
                    ref.setPath(newPath);
                }
                return Filter.CONTINUE;
            }

        };
        slashFilter.setNext(baseRouter);

        return baseRouter;
    }
}
