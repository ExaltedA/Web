import { Component, OnInit } from '@angular/core';
import {ProductService} from '../product.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  title = 'servicesGroup2';
  constructor(private productService: ProductService ) { }


  logged = false;

  username = '';
  password = '';


  ngOnInit(){
    let token = localStorage.getItem('token');
    if (token){
      this.logged = true;
      this.productService.username = this.username;
    }
  }

  login(){
    this.productService.login(this.username, this.password)
      .subscribe(res => {

        localStorage.setItem('token', res.token);

        this.logged = true;

        // this.username = '';
        // this.password = '';
      })
  }

  logout(){
    localStorage.clear();
    this.logged = false;
    this.productService.username = '';
  }
}
