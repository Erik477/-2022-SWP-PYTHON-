package Observer;

import java.util.Observable;
import java.util.Observer;

import javax.swing.JFrame;
import javax.swing.JTextField;

class Bildschirm implements Observer{
    
    private JTextField field;
    
    public Bildschirm(){
        JFrame frame = new JFrame();
        field = new JTextField("a");
        frame.add(field);
        
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 50);
        frame.setVisible(true);
    }
    
    public void update(Observable o, Object arg) {
        field.setText((String) arg);
    }
}
class Farbsignale implements Observer{
    
    private JTextField field;
    
    public Farbsignale(){
        JFrame frame = new JFrame();
        field = new JTextField("a");
        frame.add(field);
        
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 50);
        frame.setVisible(true);
    }
    
    public void update(Observable o, Object arg) {
        field.setText((String) arg);
    }
}