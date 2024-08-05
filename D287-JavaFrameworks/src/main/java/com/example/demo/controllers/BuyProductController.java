package com.example.demo.controllers;

import com.example.demo.domain.Product;
import com.example.demo.repositories.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.Optional;

@Controller
public class BuyProductController {

    @Autowired
    private ProductRepository productRepository;

    @GetMapping("/buyProduct")
    public String buyProduct(@RequestParam("productID") long productID) {

        Optional<Product> productPurchase = productRepository.findById(productID);

        if (productPurchase.isPresent()) {
            Product product = productPurchase.get();

            if (product.getInv() > 0){
                product.setInv(product.getInv() - 1);
                productRepository.save(product);
                return "buyProductSuccess";
            } else {
                return "buyProductFail";
            }
        } else {
            return "buyProductFail";
        }
    }
}
