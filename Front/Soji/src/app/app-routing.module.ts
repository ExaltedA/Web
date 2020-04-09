import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductsComponent} from './products/products.component';
import { MainComponent} from './main/main.component';
import { RouterModule, Routes } from '@angular/router';
import { ProductDetailComponent} from './product-detail/product-detail.component';


const routes: Routes = [
  { path: 'products', component: ProductsComponent },
  { path: '', component: MainComponent},
  { path: 'detail/:name', component: ProductDetailComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
