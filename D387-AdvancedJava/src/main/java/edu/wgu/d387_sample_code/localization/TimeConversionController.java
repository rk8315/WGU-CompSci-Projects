package edu.wgu.d387_sample_code.localization;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@CrossOrigin(origins = "http://localhost:4200")
@RestController
@RequestMapping("/presentationTimes")
public class TimeConversionController {

    @GetMapping("/presentations")
    public ResponseEntity<String> timeZoneConversion(){
        return new ResponseEntity<String>(TimeConversion.getTimeConversion(), HttpStatus.OK);
    }
}
