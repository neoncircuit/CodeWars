public class Cat extends Animal {
  public Cat(String name) {
    super(name);
  }
  
  @Override
  public String speak() {
    return this.name + " meows.";
  }
}