package perf;

import java.sql.*;
import java.util.*;
import java.io.*;

public class Performance {

	private Connection session;
	private String dbName;

	private ArrayList<String> queries;

	public Performance(String dbName, String queriesPath) throws IOException {
		this.queries = new ArrayList<String>();
		this.dbName = dbName;
		String jdbcPath = "jdbc:vertica://localhost:5433/" + dbName;
		initializeConnection(jdbcPath);
		readQueries(queriesPath);
	}

	private void initializeConnection(String jdbcPath) {
		try {
			Class.forName("com.vertica.jdbc.Driver");
		} catch (ClassNotFoundException e) {
			System.err.println("Could not find the JDBC driver class.\n");
    		e.printStackTrace();
            System.exit(1);
		}

		try {
			session = DriverManager.getConnection(jdbcPath, "dbadmin", "");
		} catch (SQLException e) {
			System.err.println("Could not connect to the database.\n");
			e.printStackTrace();
			System.exit(1);
		}
	}

	private void readQueries(String queriesPath) throws IOException {
		BufferedReader queryReader = new BufferedReader(new FileReader(queriesPath));
		for(int i = 0; ; i++) {
			String query = null;
			if((query = queryReader.readLine()) == null) break;
			System.out.println("Query = [" + query + "]");
			queries.add(query);
		}
		queryReader.close();
	}

	public void latencyBenchmark() throws IOException, SQLException {
		BufferedWriter resWriter = new BufferedWriter(new FileWriter("latency_results_regex"));
		long t0, tdiff;
		Statement stmt = session.createStatement();
		for(int i = 0; i < queries.size(); i++) {
			String query = queries.get(i);
				for(int j = 0; j < 10; j++) {
				long count = 0;
				try {
					t0 = System.nanoTime();
					ResultSet res = stmt.executeQuery(query);
					while(res.next()) count++;
					tdiff = (System.nanoTime() - t0) / 1000;
					resWriter.write(i + "\t" + j + "\t" + count + "\t" + tdiff);
				} catch (Exception e) {
					System.err.println("Malformed query\n");
				}
			}
		}
		resWriter.close();
	}

	public static void main(String[] args) throws IOException, SQLException, InterruptedException {
		String dbName = args[0];
		Performance perf = new Performance(args[0], args[1]);
		perf.latencyBenchmark();
	}
}
