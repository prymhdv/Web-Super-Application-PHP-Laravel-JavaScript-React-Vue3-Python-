<?php

namespace App\Http\Controllers;

 
use Illuminate\Http\Request;
use App\Http\Requests;
use App\Http\Controllers\Controller;
use App\Models\Ajax;
use Illuminate\Support\Facades\Response as Response;

class AjaxController extends Controller
{
    public function index2()
    {
        $msg = "This is a simple message.";
        return response()->json(array('msg' => $msg), 200);
    }
    public function index()
    {
        $projects = Ajax::orderBy('id', 'desc')->get();
        return view('ajax')->with(compact('projects'));
    }

    /**
     * Store a newly created resource in storage.
     *
     */
    public function store(Request $request)
    {
        $data = $request->validate([
            'title' => 'required',
            'description' => 'required'
        ]);

        $project = Ajax::create($data);

        return Response::json($project);
    }
}
