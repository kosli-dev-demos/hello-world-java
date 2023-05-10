import static org.junit.Assert.assertEquals;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.InetSocketAddress;
import java.net.URL;

import com.sun.net.httpserver.HttpServer;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class HelloWorldAPITest {

    private HttpServer server;
    private URL base;

    @Before
    public void setUp() throws Exception {
        server = HttpServer.create(new InetSocketAddress(0), 0);
        server.createContext("/hello", new HelloWorldAPI.MyHandler("./src/main/resources/config.properties"));
        server.setExecutor(null);
        server.start();
        int port = server.getAddress().getPort();
        base = new URL("http://localhost:" + port);
    }

    @After
    public void tearDown() throws Exception {
        server.stop(0);
    }

    @Test
    public void testHelloWorldAPI() throws IOException {
        HttpURLConnection conn = (HttpURLConnection) new URL(base, "/hello").openConnection();
        conn.setRequestMethod("GET");
        conn.connect();
        try (InputStream in = conn.getInputStream()) {
            byte[] response = in.readAllBytes();
            assertEquals("{\"message\": \"Hello There\"}", new String(response));
        }
    }
}