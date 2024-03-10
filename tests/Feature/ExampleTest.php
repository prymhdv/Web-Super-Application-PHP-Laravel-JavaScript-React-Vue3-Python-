<?php

namespace Tests\Feature;

// use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;
use App\Models\Shopping\Title;
class ExampleTest extends TestCase
{
    /**
     * A basic test example.
     */
    public function test_the_application_returns_a_successful_response(): void
    {
        $response = $this->get('/');

        $response->assertStatus(200);
    }

    public function testNewClientForm(){     //cheack professor is in view or not
        $response=$this->get('/clients/new');
        $response->assertStatus(200);
    }

    public function testProfessorOption(){
        $response=$this->get('/clients/new');
        $this-> assertContains('Professor',
            $response->getContent(),
            'HTML should have Professor'
        );
    }
}
