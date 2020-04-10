import { Component, OnInit } from '@angular/core';
import {CartService} from '../cart.service';
import {Product} from '../product';
import { FormBuilder } from '@angular/forms';
import {Order} from '../order';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {
  products: Product[];
  checkoutForm;
  constructor( private cartService: CartService,
               private formBuilder: FormBuilder) {
    this.checkoutForm = this.formBuilder.group({
      name: '',
      address: ''
    });
  }

  ngOnInit(): void {
    this.getProducts();
  }
  getProducts(): void {
    this.products = this.cartService.getProducts();
  }
  onSubmit(customerData) {
    this.products = this.cartService.clearCart();
    this.checkoutForm.reset();

    this.cartService.submitForm(customerData);

    console.warn('Your order has been submitted', customerData);
  }
}
