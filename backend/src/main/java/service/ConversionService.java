package service;

import org.springframework.stereotype.Service;

import controller.ConversionController;

@Service
public class ConversionService {
    private final ConversionController conversionController;

    public ConversionService(ConversionController conversionController){
        this.conversionController = conversionController;
    }
}
