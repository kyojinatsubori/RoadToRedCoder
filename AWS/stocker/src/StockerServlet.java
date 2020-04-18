import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class StockerServlet
 */
@WebServlet("/")
public class StockerServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

    /**
     * @see HttpServlet#HttpServlet()
     */
    public StockerServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		String page="";
	    req.setCharacterEncoding("UTF-8");
	    String function = req.getParameter("function");
	    String name;
	    int amount;
	    int price;
	    StockerDAO dao = new StockerDAO("user", "candidate");
	    try {
	    	dao.connect();
	    	switch (function) {
	    		case "addstock":
	    			name = req.getParameter("name");
	    			if (req.getParameter("amount") == null) {
	    				amount = 1;
	    			}else {
	    				amount = Integer.parseInt(req.getParameter("amount"));
	    			}
	    			dao.addStock(name, amount);
	    			break;
	    		case "checkstock":
	    			ArrayList<Product> ps;
	    			if (req.getParameter("name") == null) {
	    				ps = dao.checkStock();
	    			}else {
	    				name = req.getParameter("amount");
	    				ps = dao.checkStock(name);
	    			}
	    			req.setAttribute("ans", ps);
	    			page="/Stock.jsp";
	    			break;
	    		case "sell":
	    			name = req.getParameter("name");
	    			if (req.getParameter("amount")==null) {
	    				amount = 1;
	    			}else {
	    				amount = Integer.parseInt(req.getParameter("amount"));
	    			}
	    			if (req.getParameter("price")==null) {
	    				price = 0;
	    			}else {
	    				price = Integer.parseInt(req.getParameter("price"));
	    			}
	    			dao.sell(name, amount, price);
	    			break;
	    		case "checksales":
	    			req.setAttribute("ans", dao.checkSales());
	    			page = "/Sales.jsp";
	    			break;
	    		case "deleteall":
	    			dao.deleteAll();
	    			break;
	    	}
	    }catch (SQLException e) {
	    	e.printStackTrace();
	    }finally {
	    	try {
	    		dao.close();
	    	}catch (SQLException e){
	    		e.printStackTrace();
	    	}
	    }
	    if (page != "") {
	    	RequestDispatcher rd = req.getRequestDispatcher(page);
	    	rd.forward(req, res);
	    }
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
