import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {ReactiveFormsModule} from '@angular/forms';

import { AppRoutingModule} from './app-routing.module';
import { AppComponent } from './app.component';
import { ProductsComponent } from './products/products.component';
import { MainComponent } from './main/main.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { HttpClientModule } from '@angular/common/http';
import { HttpClientInMemoryWebApiModule } from 'angular-in-memory-web-api';
import { InMemoryDataService } from './in-memory-data.service';
import { ProductDetailComponent } from './product-detail/product-detail.component';
import { FeaturedprodComponent } from './featuredprod/featuredprod.component';
import { ProductSearchComponent } from './product-search/product-search.component';
import { CartComponent } from './cart/cart.component';
import { DeliveryComponent } from './delivery/delivery.component';


@NgModule({
  declarations: [
    AppComponent,
    ProductsComponent,
    MainComponent,
    TopBarComponent,
    ProductDetailComponent,
    FeaturedprodComponent,
    ProductSearchComponent,
    CartComponent,
    DeliveryComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    HttpClientInMemoryWebApiModule.forRoot(
      InMemoryDataService, { dataEncapsulation: false }
    ),
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
