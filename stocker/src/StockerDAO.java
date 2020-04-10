
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

public class StockerDAO {

	private Connection con;
	private String user;
	private String password;

	public StockerDAO(String user, String password) {
		this.user = user;
		this.password = password;
	}

	public void connect() throws SQLException{
		String url = "jdbc:mysql://localhost:3306/aws";
		con = DriverManager.getConnection(url, user, password);
	}

	public void close() throws SQLException{
		if(con != null) {
			con.close();
		}
	}

	public void addStock(String name, int amount) throws SQLException{
		ResultSet res = null;
		PreparedStatement stmt = null;
		Product p = null;
		String sql1 = "select * from STOCK where name = ?";
		String sql2 = "update STOCK set amount = amount + ? where name = ?";
		String sql3 = "insert into STOCK values(?, ?)";

		try {
			stmt = con.prepareStatement(sql1);
			stmt.setString(1, name);
			res = stmt.executeQuery();
			if (res.next()) {
				p = new Product();
				p.setName(res.getString(1));
				p.setAmount(res.getInt(2));
			}
		}finally {
			if (res != null) {
				res.close();
			}
			if (stmt != null) {
				stmt.close();
			}
		}

		if (p != null) {
			try {
				stmt = con.prepareStatement(sql2);
				stmt.setInt(1, amount);
				stmt.setString(2, name);
				stmt.executeUpdate();
			}finally {
				if (res != null) {
					res.close();
				}
				if (stmt != null) {
					stmt.close();
				}
			}
		}else {
			try {
				stmt = con.prepareStatement(sql3);
				stmt.setString(1, name);
				stmt.setInt(2, amount);
				stmt.executeUpdate();
			}finally {
				if (res != null) {
					res.close();
				}
				if (stmt != null) {
					stmt.close();
				}
			}
		}
	}

	public ArrayList<Product> checkStock(String name) throws SQLException{
		ResultSet res = null;
		PreparedStatement stmt = null;
		ArrayList<Product> ps = new ArrayList<Product>();
		String sql = "select * from STOCK where name = ? ";

		try {
			stmt = con.prepareStatement(sql);
			stmt.setString(1, name);
			res = stmt.executeQuery();
			while (res.next()) {
				Product p = new Product();
				p.setName(res.getString(1));
				p.setAmount(res.getInt(2));
				ps.add(p);
			}
		}finally {
			if (res != null) {
				res.close();
			}
			if (stmt != null) {
				stmt.close();
			}
		}
		return ps;
	}

	public ArrayList<Product> checkStock() throws SQLException{
		ResultSet res = null;
		PreparedStatement stmt = null;
		ArrayList<Product> ps = new ArrayList<Product>();
		String sql = "select * from STOCK order by name";

		try {
			stmt = con.prepareStatement(sql);
			res = stmt.executeQuery();
			while (res.next()) {
				Product p = new Product();
				p.setName(res.getString(1));
				p.setAmount(res.getInt(2));
				ps.add(p);
			}
		}finally {
			if (res != null) {
				res.close();
			}
			if (stmt != null) {
				stmt.close();
			}
		}
		return ps;
	}

	public void sell(String name, int amount, int price) throws SQLException{
		PreparedStatement stmt = null;
		String sql1 = "update STOCK set amount = amount - ? where name = ?";
		String sql2 = "update SALES set sales = sales + ?";

		try {
			stmt = con.prepareStatement(sql1);
			stmt.setInt(1, amount);
			stmt.setString(2,  name);
			stmt.executeUpdate();
		}finally {
			if (stmt != null) {
				stmt.close();
			}
		}

		try {
			stmt = con.prepareStatement(sql2);
			stmt.setInt(1, amount * price);
			stmt.executeUpdate();
		}finally {
			if (stmt != null) {
				stmt.close();
			}
		}


	}

	public int checkSales() throws SQLException{
		ResultSet res = null;
		PreparedStatement stmt = null;
		String sql = "select sales from SALES";
		int sales = 0;
		try {
			stmt = con.prepareStatement(sql);
			res = stmt.executeQuery();
			if (res.next()) {
				sales = res.getInt(1);
			}
		}finally {
			if (res != null) {
				res.close();
			}
			if (stmt != null) {
				stmt.close();
			}
		}
		return sales;
	}

	public void deleteAll() throws SQLException{
		PreparedStatement stmt = null;
		String sql1 = "delete from STOCK";
		String sql2 = "delete from SALES";

		try {
			stmt = con.prepareStatement(sql1);
			stmt.executeUpdate();
		}finally {
			if (stmt != null) {
				stmt.close();
			}
		}

		try {
			stmt = con.prepareStatement(sql2);
			stmt.executeUpdate();
		}finally {
			if (stmt != null) {
				stmt.close();
			}
		}
	}

}
