import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public login = true;
  constructor() { }

  ngOnInit(): void {
  }
  switchTrue() {
    this.login = true;
  }
  switchFalse() {
    this.login = false;
  }
}
