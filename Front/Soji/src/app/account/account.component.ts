import {Component, Input, OnInit} from '@angular/core';
import {User} from '../user';
import { AccountService} from '../account.service';
import {Product} from '../product';

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css']
})
export class AccountComponent implements OnInit {
  @Input() user: User;
  usera:User = {name: 'Aldik', surname: 'Yessenturov', city: 'Kokshetau', password: 'fsociety2', username: 'hi'}

  constructor(private accountService: AccountService) { }
  ngOnInit(): void {
  }

}
