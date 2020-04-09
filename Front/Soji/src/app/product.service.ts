import { Injectable } from '@angular/core';
import { Product} from './product';
import { PRODUCTS} from './mock';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor() { }

  getProducts(): Observable<Product[]> {
    return of(PRODUCTS);
  }
  getProduct(name: string): Observable<Product> {
    return of(PRODUCTS.find(product => product.name === name));
  }
}
