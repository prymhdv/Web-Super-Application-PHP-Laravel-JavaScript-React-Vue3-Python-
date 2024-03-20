<?php

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;
use phpDocumentor\Reflection\Types\Boolean;

class TaskResource extends JsonResource
{
    /**
     * Transform the resource into an array.       php artisan make:resource TaskResource
     *
     * @return array<string, mixed>
     */
    public function toArray(Request $request): array
    {
        //return parent::toArray($request);
        return [
            'id'            => $this->id,
            'name'          => $this->name,
            'is_completed'  => (Boolean)$this->is_completed, 
        ];
    }
}
