package edu.wgu.d387_sample_code.localization;

import java.util.Locale;
import java.util.ResourceBundle;

public class WelcomeMessage implements Runnable {

    Locale locale;

    public WelcomeMessage(Locale locale) {
        this.locale = locale;
    }

    public String getWelcomeMessage() {
        ResourceBundle resourceBundle = ResourceBundle.getBundle("translation", locale);
        return resourceBundle.getString("welcomeMessage");
    }

    @Override
    public void run(){
        System.out.println("Thread: " + Thread.currentThread().getName() +
                            " | ID: " + Thread.currentThread().getId() +
                            " | Message: " + getWelcomeMessage());
    }
}
