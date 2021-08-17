import Menu from './Menu';
import './css/style.css';
import './css/font-awesome.min.css';
import './css/responsive.css';
import './css/default.css';

function Header(props) {
    return (
    <div>
	    <div class="page-loader">
			<p class="wait"> Please Wait.. </p>
	    	<div class="loader-in"></div>
	    </div>
	    <div class="pageWrapper">

			<div class="login-box">
				<a class="close-login" href="#"><i class="fa fa-times"></i></a>
				<form>
					<div class="container">
						<p>Hello our valued visitor, We present you the best web solutions and high quality graphic designs with a lot of features. just login to your account and enjoy ...</p>
						<div class="login-controls">
							<div class="skew-25 input-box left">
								<input type="text" class="txt-box skew25" placeholder="User name Or Email" />
							</div>
							<div class="skew-25 input-box left">
								<input type="password" class="txt-box skew25" placeholder="Password" />
							</div>
							<div class="left skew-25 main-bg">
								<input type="submit" class="btn skew25" value="Login" />
							</div>
							<div class="check-box-box">
								<input type="checkbox" class="check-box" /><label>Remember me !</label>
								<a href="#">Forgot your password ?</a>
							</div>
						</div>
					</div>
				</form>
			</div>
        
			<div id="headWrapper" class="clearfix">		    	
		    	
		    	<div class="top-bar">
				    <div class="container">
						<div class="row">
							<div class="cell-5">
							    <ul>
								    <li><a href="#"><i class="fa fa-envelope"></i>info@it-rays.com</a></li>
								    <li><span><i class="fa fa-phone"></i> Call Us: +1 (888) 000-0000</span></li>
							    </ul>
							</div>
							<div class="cell-7 right-bar">
					    		<ul class="right">
						    	    <li><a href="cart.html"><i class="fa fa-shopping-cart"></i>0 item(s) - $0.00</a></li>
						    	    <li><a href="siteMap.html"><i class="fa fa-sitemap"></i>Site Map</a></li>
						    	    <li><a href="register.html"><i class="fa fa-user"></i>Register</a></li>
						    	    <li><a href="#" class="login-btn"><i class="fa fa-unlock-alt"></i> Login</a></li>
									<li><a href="#" class="login-btn"><i class="fa fa-flag"></i> English</a></li>
						        </ul>
							</div>
						</div>
				    </div>
			    </div>
			</div>
		</div>
		<Menu />
	</div>);
}
export default Header;