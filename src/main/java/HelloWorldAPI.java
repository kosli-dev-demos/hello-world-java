import java.io.FileInputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Properties;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

public class HelloWorldAPI {
    public static void main(String[] args) throws Exception {
        if (args.length < 1) {
            System.err.println("Please specify the path to the configuration file.");
            System.exit(1);
        }
        String configFilePath = args[0];
        HttpServer server = HttpServer.create(new InetSocketAddress(80), 0);
        server.createContext("/hello", new MyHandler(configFilePath));
        server.setExecutor(null);
        server.start();
    }

    static class MyHandler implements HttpHandler {
        private final Properties props;

        public MyHandler(String configFilePath) throws IOException {
            props = new Properties();
            props.load(Files.newInputStream(Paths.get(configFilePath)));
        }

        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (!"GET".equals(exchange.getRequestMethod())) {
                exchange.sendResponseHeaders(405, -1); // Method Not Allowed
                exchange.close();
                return;
            }
            String message = props.getProperty("message");
            String response = "{\"message\": \"" + message + "\"}";
            exchange.getResponseHeaders().set("Content-Type", "application/json");
            exchange.sendResponseHeaders(200, response.length());
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
}
