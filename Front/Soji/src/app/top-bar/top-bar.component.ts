import { Component, OnInit } from '@angular/core';
import {ProductService} from '../product.service';

@Component({
  selector: 'app-top-bar',
  templateUrl: './top-bar.component.html',
  styleUrls: ['./top-bar.component.css']
})
export class TopBarComponent implements OnInit {
  logged = false;
  userName: string;
  constructor(private productService: ProductService) { }


  ngOnInit(): void {
    this.getUsername()
  }
  getUsername(): void{
    this.userName =this.productService.username;
   if(this.userName){
     this.logged = true;
   }
  }
}
