import {Component, Input, OnInit} from '@angular/core';
import {User} from '../user';
import { AccountService} from '../account.service';
import {Product} from '../product';
import {Order} from '../order';
import {ReviewsService} from '../reviews.service';

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css']
})
export class AccountComponent implements OnInit {
  @Input() user: User;
  // @ts-ignore
  usera: User = {name: 'Aldik', surname: 'Yessenturov', city: 'Kokshetau', password: 'fsociety2', username: 'hi'}

  orders: Order[];
  order: Order;
  constructor(private reviewsService: ReviewsService) { }

  ngOnInit(): void {
    this.getOrders();
  }
  getOrders(): void {
    this.reviewsService.getOrders().subscribe(orders => this.orders = orders);
  }
}

