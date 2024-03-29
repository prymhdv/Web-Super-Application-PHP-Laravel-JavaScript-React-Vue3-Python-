<?php

namespace App\Models;

use Illuminate\Notifications\Notifiable;
use Illuminate\Foundation\Auth\User as Authenticatable;
use App\Notifications\CustomPasswordReset;
use Illuminate\Database\Eloquent\Factories\HasFactory;

class User extends Authenticatable 
{   use HasFactory;
    use Notifiable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name', 'email', 'password',
    ];

    /**
     * The attributes that should be hidden for arrays.
     *
     * @var array
     */
    protected $hidden = [
        'password', 'remember_token',
    ];
    
	 public function posts()
    {
        return $this->hasMany('App\Models\Blog\Post');
    }

    public function sendPasswordResetNotification($token)
    {
        $this->notify(new CustomPasswordReset($token));


    }

    public function role(){

        return $this->belongsTo('App\Models\Role');
    }

    //public function isAdmin($role){
    public function isAdmin(){

        //if($this->role->name == $role)
        if($this->role->name == 'administrator'){
           //dd('$this->role->name == administrator');
            return true;
        }
        return false;
     
    }
}
