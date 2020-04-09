import { Component, OnInit } from '@angular/core';
import { Product} from '../product';
import {PRODUCTS} from '../mock';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {
  products = PRODUCTS;
  selectedProd: Product;


  constructor() { }

  ngOnInit(): void {
  }
  onSelect(product: Product): void {
    this.selectedProd = product;
  }
}
