<?php

namespace App\Models\Shopping;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Title extends ReadOnlybase
{
    use HasFactory;
    protected $titles_array = ['Mr','Mrs','Ms','Dr','Mx'];
}
