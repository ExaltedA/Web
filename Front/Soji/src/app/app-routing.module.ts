import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductsComponent} from './products/products.component';
import { MainComponent} from './main/main.component';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: 'products', component: ProductsComponent },
  { path: '', component: MainComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
