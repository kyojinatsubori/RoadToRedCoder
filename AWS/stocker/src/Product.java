
public class Product {
	private String name;
	private int amount;

	public Product() {

	}
	public Product(String name, int amount) {
		this.amount = amount;
		this.name = name;
	}

	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAmount() {
		return amount;
	}
	public void setAmount(int amount) {
		this.amount = amount;
	}

}
