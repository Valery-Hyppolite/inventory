# Inventory System
Introducing an inventory management system designed to efficiently track products, orders, and customers. With real-time updates, you can stay on top of your inventory, orders, and profits effortlessly. The system automatically calculates profits and losses, giving you valuable insights into the financial performance of each product and your overall store. Seamlessly packaged with docker-compose, this web application is deployed on AWS EC2 within a secure Virtual Private Cloud (VPC) environment.

## # Features
* Add, update, and delete products and customers.
* Automatically calculate profits and losses anytime changes occur such as new orders, updating products, new customers ect...
* Check customers' information and see all orders associated with each customer. 

## # Deployement
* Deployed infracture as code using terraform
* Created both a local and deployment docker file
* Packaged project with docker-compose
* Deployed project on AWS EC2 instance with docker



### Dashboard preview of your system.
![in1](https://user-images.githubusercontent.com/83102811/183741664-d5e785f8-b8c9-4f9a-9134-572d99857691.png)

### Inventory of each product in stock and their revenue.
![in2](https://user-images.githubusercontent.com/83102811/183746658-71ac2104-55dc-4774-836b-970a7a8d4f94.png)

### Customer order history
![dash1](https://user-images.githubusercontent.com/83102811/212495699-88cf3943-68fc-436e-a029-aefb7bdb91ca.png)

### Order information
![dash2](https://user-images.githubusercontent.com/83102811/212495733-53a0e45e-a8d0-48d8-86f5-f1f07cdbf364.png)