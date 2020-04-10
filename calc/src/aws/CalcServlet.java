package aws;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;



/**
 * Servlet implementation class AWSServlet
 */
@WebServlet("/")
public class CalcServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

    /**
     * @see HttpServlet#HttpServlet()
     */
    public CalcServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		// TODO Auto-generated method stub

	    String page = "/calc.jsp";
	    req.setCharacterEncoding("UTF-8");
	    String formula = req.getQueryString();
	    calc c = new calc();
	    System.out.println(formula);
	    formula = c.chkFormula(formula);
	    System.out.println(formula);
	    if (!formula.equalsIgnoreCase("ERROR")){
		    System.out.println(formula);
	    	formula=c.calclation(formula);
		    System.out.println(formula);
	    }
	    req.setAttribute("formula", formula);
	    RequestDispatcher rd = req.getRequestDispatcher(page);
	    rd.forward(req, res);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
