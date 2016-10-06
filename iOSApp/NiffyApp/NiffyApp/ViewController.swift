//
//  ViewController.swift
//  NiffyApp
//
//  Created by Joao on 06/10/16.
//  Copyright © 2016 João Colaço. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet var webView: UIWebView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        // Do any additional setup after loading the view, typically from a nib.
        let url = URL(string: "https://apps.roadworks.org");
        let requestObj = URLRequest(url: url!);
        webView.loadRequest(requestObj);
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

}

