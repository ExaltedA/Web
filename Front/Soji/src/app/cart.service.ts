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
  submitForm(form) {
    const formData: any = new FormData();
    formData.append('name', form.get('name').value);
    formData.append('address', form.get('address').value);

    this.http.post('api/submit-order', formData).subscribe(
      (response) => console.log(response),
      (error) => console.log(error)
    );
  }
  clearCart() {
    this.products = [];
    return this.products;
  }

  constructor(private http: HttpClient) { }
}
