package edu.wgu.d387_sample_code.localization;

import org.springframework.web.bind.annotation.CrossOrigin;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

@CrossOrigin(origins = "https://localhost:4200")
public class TimeConversion {

    public static String getTimeConversion() {

        ZoneId zEastern = ZoneId.of("America/New_York");
        ZoneId zMountain = ZoneId.of("America/Denver");
        ZoneId zUniversal = ZoneId.of("UTC");

        ZonedDateTime easternDateTime = ZonedDateTime.now(zEastern);
        ZonedDateTime mountainDateTime = ZonedDateTime.now(zMountain);
        ZonedDateTime universalDateTime = ZonedDateTime.now(zUniversal);

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("hh:mm a");

        String timeConversions = easternDateTime.format(formatter) + " ET | " +
                                mountainDateTime.format(formatter) + " MT | " +
                                universalDateTime.format(formatter) + " UTC";

        return timeConversions;
    }
}
