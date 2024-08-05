package com.example.demo.bootstrap;

import com.example.demo.domain.InhousePart;
import com.example.demo.domain.OutsourcedPart;
import com.example.demo.domain.Part;
import com.example.demo.domain.Product;
import com.example.demo.repositories.OutsourcedPartRepository;
import com.example.demo.repositories.PartRepository;
import com.example.demo.repositories.ProductRepository;
import com.example.demo.service.OutsourcedPartService;
import com.example.demo.service.OutsourcedPartServiceImpl;
import com.example.demo.service.ProductService;
import com.example.demo.service.ProductServiceImpl;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Optional;

/**
 *
 *
 *
 *
 */
@Component
public class BootStrapData implements CommandLineRunner {

    private final PartRepository partRepository;
    private final ProductRepository productRepository;

    private final OutsourcedPartRepository outsourcedPartRepository;

    public BootStrapData(PartRepository partRepository, ProductRepository productRepository, OutsourcedPartRepository outsourcedPartRepository) {
        this.partRepository = partRepository;
        this.productRepository = productRepository;
        this.outsourcedPartRepository=outsourcedPartRepository;
    }

    @Override
    public void run(String... args) throws Exception {

       /*
        OutsourcedPart o= new OutsourcedPart();
        o.setCompanyName("Western Governors University");
        o.setName("out test");
        o.setInv(5);
        o.setPrice(20.0);
        o.setId(100L);
        outsourcedPartRepository.save(o);
        OutsourcedPart thePart=null;
        List<OutsourcedPart> outsourcedParts=(List<OutsourcedPart>) outsourcedPartRepository.findAll();
        for(OutsourcedPart part:outsourcedParts){
            if(part.getName().equals("out test"))thePart=part;
        }

        System.out.println(thePart.getCompanyName());
        */

        OutsourcedPart flour = new OutsourcedPart();
        flour.setCompanyName("King Arthur Baking Company");
        flour.setName("Flour");
        flour.setInv(20);
        flour.setPrice(0.40);
        flour.setId(100L);
        flour.setMaximumInv(100);
        flour.setMinimumInv(1);

        OutsourcedPart sugar = new OutsourcedPart();
        sugar.setCompanyName("Domino Foods");
        sugar.setName("Sugar");
        sugar.setInv(50);
        sugar.setPrice(.10);
        sugar.setId(200L);
        sugar.setMaximumInv(100);
        sugar.setMinimumInv(1);

        OutsourcedPart yeast = new OutsourcedPart();
        yeast.setCompanyName("Fleischmann's Yeast");
        yeast.setName("Yeast");
        yeast.setInv(70);
        yeast.setPrice(.04);
        yeast.setId(300L);
        yeast.setMaximumInv(100);
        yeast.setMinimumInv(1);

        OutsourcedPart salt = new OutsourcedPart();
        salt.setCompanyName("Morton Salt");
        salt.setName("Salt");
        salt.setInv(80);
        salt.setPrice(.05);
        salt.setId(400L);
        salt.setMaximumInv(100);
        salt.setMinimumInv(1);

        InhousePart water = new InhousePart();
        water.setName("Water");
        water.setInv(90);
        water.setPrice(0.80);
        water.setPartId(600);
        water.setMaximumInv(100);
        water.setMinimumInv(1);

        List<OutsourcedPart> outsourcedParts=(List<OutsourcedPart>) outsourcedPartRepository.findAll();
        for(OutsourcedPart part:outsourcedParts){
            System.out.println(part.getName()+" "+part.getCompanyName());
        }

        Product whiteLoaf = new Product(1000, "White Loaf",6.99, 25);
        Product sourDough = new Product(1001, "Sour Dough", 10.00,15);
        Product scallionBun = new Product(1002, "Scallion Bun", 5.00, 30);
        Product pretzel = new Product(1003, "Pretzel", 3.99, 50);
        Product baguette = new Product(1004, "Baguette", 7.99,20);

        if(productRepository.count() == 0 && partRepository.count() == 0){
            partRepository.save(flour);
            partRepository.save(sugar);
            partRepository.save(yeast);
            partRepository.save(salt);
            partRepository.save(water);
            productRepository.save(whiteLoaf);
            productRepository.save(sourDough);
            productRepository.save(scallionBun);
            productRepository.save(pretzel);
            productRepository.save(baguette);
        }

        /*
        Product bicycle= new Product("bicycle",100.0,15);
        Product unicycle= new Product("unicycle",100.0,15);
        productRepository.save(bicycle);
        productRepository.save(unicycle);
        */

        System.out.println("Started in Bootstrap");
        System.out.println("Number of Products"+productRepository.count());
        System.out.println(productRepository.findAll());
        System.out.println("Number of Parts"+partRepository.count());
        System.out.println(partRepository.findAll());

    }
}
