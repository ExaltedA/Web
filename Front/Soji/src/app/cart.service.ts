import { Injectable } from '@angular/core';
import { Product} from './product';
import { HttpClient } from '@angular/common/http';
import {Order} from './order';


@Injectable({
  providedIn: 'root'
})
export class CartService {
  products: Product[] = [];
  orders: Order;
  addToCart(product: Product) {
    this.products.push(product);
  }

  getProducts() {
    return this.products;
  }

  clearCart() {
    this.products = [];
    return this.products;
  }

  constructor(private http: HttpClient) { }
}
