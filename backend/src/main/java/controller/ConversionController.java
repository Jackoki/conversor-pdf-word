package controller;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;



@RestController
public class ConversionController {
    @GetMapping("/")
    public String getArchive() {
        return new String();
    }

    @PostMapping("/")
    public String sendArchive(String entity) {
        return "";
    }
    
    
}
