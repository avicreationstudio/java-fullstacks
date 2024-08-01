# files

## Pre-requisite

- `java`
  - getter
  - setter
  - `List<Product>`
- back-end theory concepts
  - Rest API link with HTTP Methods
  - Routing
  - Request Body
  - path variable
  - CRUD
  - ORM ( object relation model ) : Hibernate

## do follow same order as below

1. Entity
1. Repository
1. Service
1. Controller

### `entity/Product.java`

```java
package com.SimpleProject.back_end_api.entity;

import jakarta.persistence.*;
import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "product")
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String name;
    private String description;
    private double price;
}
```

### `repository/ProductRepository.java`

```java
package com.SimpleProject.back_end_api.respository;

import com.SimpleProject.back_end_api.entity.Product;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductRepository extends JpaRepository<Product, Integer> {
}
```

### `service/ProductService.java`

```java
package com.SimpleProject.back_end_api.service;

import com.SimpleProject.back_end_api.entity.Product;
import com.SimpleProject.back_end_api.respository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProductService {
    @Autowired
    private ProductRepository productRepository;

//    C:  create
    public Product addProduct(Product product) {
        return productRepository.save(product);
    }

//    R:  read
    public List<Product> getAllProduct() {
        return productRepository.findAll();
    }
//    U:  Update
    public Product updateProduct(Product product) {
        Product existingProduct = productRepository.findById(product.getId()).orElse(null);
        if(existingProduct == null) {
            return null;
        }
        existingProduct.setName(product.getName());
        existingProduct.setDescription(product.getDescription());
        existingProduct.setPrice(product.getPrice());
        return productRepository.save(existingProduct);
    }
//    D:  Delete
    public String deleteById(int id){
        Product existingProduct = productRepository.findById(id).orElse(null);
        if (existingProduct == null) {
            return "item with id not found";
        }
        productRepository.deleteById(id);
        return "Removed product id :" + id;
    }

}

```

### `controller/ProductController`

```java
package com.SimpleProject.back_end_api.controller;

import com.SimpleProject.back_end_api.entity.Product;
import com.SimpleProject.back_end_api.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class ProductController {
    @Autowired
    private ProductService productService;

//    C
    @PostMapping("/product")
    public Product addProduct(@RequestBody Product product) {
        return productService.addProduct(product);
    }
//    R
    @GetMapping("/product")
    public List<Product> getAllProduct() {
        return productService.getAllProduct();
    }
//    U
    @PutMapping("/product")
    public Product updateProduct(@RequestBody Product product) {
        return productService.updateProduct(product);
    }
//    D
    @DeleteMapping("/product/{id}")
    public String deleteProduct(@PathVariable int id) {
        return productService.deleteById(id);
    }
}

```
