<?php

namespace Tests\Unit;

use PHPUnit\Framework\TestCase;
use App\Models\Shopping\Title;

class ExampleTest extends TestCase
{
    /**
     * A basic test example.
     */
    public function test_that_true_is_true(): void
    {
        $this->assertTrue(true);
    }

    public function testTitleModelCount(){
        $title = new Title;
        // $value = 2;
        // $this->assertTrue(1==$value, 'Value Should be 1');
        $this->assertTrue(count($title->all()) === 6 , 'It Should have 6 titles');
    }

    public function testLastTitleShouldBeProfessro(){
        $titles = new Title;
        $titles_array = $titles->all();
        $this->assertEquals('Professor',array_pop($titles_array),'Titles last element should be professor');

    }
}
