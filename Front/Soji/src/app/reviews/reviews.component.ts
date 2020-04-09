import { Component, OnInit } from '@angular/core';
import {Review} from '../review';
import {ReviewsService} from '../reviews.service';
import {Product} from '../product';

@Component({
  selector: 'app-reviews',
  templateUrl: './reviews.component.html',
  styleUrls: ['./reviews.component.css']
})
export class ReviewsComponent implements OnInit {
  reviews: Review[];
  constructor(private reviewsService: ReviewsService) { }

  ngOnInit(): void {
    this.getReviews();
  }
  getReviews(): void {
    this.reviewsService.getReviews().subscribe(reviews => this.reviews = reviews);
  }
}
