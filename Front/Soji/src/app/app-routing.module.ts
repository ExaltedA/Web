import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductsComponent} from './products/products.component';
import { MainComponent} from './main/main.component';
import { RouterModule, Routes } from '@angular/router';
import { ProductDetailComponent} from './product-detail/product-detail.component';
import {CartComponent} from './cart/cart.component';
import {DeliveryComponent} from './delivery/delivery.component';

const routes: Routes = [
  { path: 'products', component: ProductsComponent },
  { path: '', component: MainComponent},
  { path: 'detail/:id', component: ProductDetailComponent },
  {path: 'cart', component: CartComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
