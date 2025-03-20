import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { ArchiveComponent } from './components/archive/archive.component';

const routes: Routes = [
  { path: '', component: HomeComponent }, // Default route without language
  { path: 'proyectos', component: ArchiveComponent }, // No language prefix
  { path: '**', pathMatch: 'full', redirectTo: '' }, // Redirect to home
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, {})
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
