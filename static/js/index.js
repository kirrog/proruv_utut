const isObjectEmpty = (objectName) => {
  return Object.keys(objectName).length === 0
}

function print_empty_table() {
	var defect_table = document.getElementById("defect-table");
 	var defect_tbody = defect_table.getElementsByTagName("tbody")[0];

  	var new_tbody = document.createElement('tbody');
	var newRow = new_tbody.insertRow();

	var newCell = newRow.insertCell();
	newCell.className = "defect-class";
	var newText = document.createTextNode('-');
	newCell.appendChild(newText);

	var newCell = newRow.insertCell();
	newCell.className = "defect-sign";
	var newText = document.createTextNode('-');
	newCell.appendChild(newText);

	var newCell = newRow.insertCell();
	newCell.className = "defect-comment";
	var newText = document.createTextNode('-');
	newCell.appendChild(newText);
	
	var newCell = newRow.insertCell();
	newCell.className = "defect-color";
	var newText = document.createTextNode('-');
	newCell.appendChild(newText);

	defect_table.replaceChild(new_tbody, defect_tbody);
}

class Img_anchor{
	constructor(id, img_name) {
		this.id = id;
		this.img_name = img_name;

		this.defect_table = {};
		this.img_colored = {};
		this.laptop_name = {};
		this.laptop_descr = {};
	}
}



let image_arr = [];
let image_arr_tmp = [];
let unique_id = 1;
let curr_id = 0;

function ss_elem_on_click(event) {
	var defect_img_box = document.getElementById("defect-img");
	var defect_table = document.getElementById("defect-table");

	defect_img_box.innerHTML = `<div class='loader'></div>`;
	print_empty_table();

	const r = /\d+/;
	var ss_elem_id = event.target.id.match(r)[0];
	curr_id = ss_elem_id; 
	
	for (const img_anchor of image_arr) {
		if (img_anchor.id == ss_elem_id) {
			if (isObjectEmpty(img_anchor.defect_table)) {
				// Get data from back

				// print new table
			} else {
				$("#defect-table").html(img_anchor.defect_table);
			}
			
			if (!isObjectEmpty(img_anchor.img_colored)) {
				//print image
			}

			if (!isObjectEmpty(img_anchor.laptop_name)) {
				$('#defect-img-label').text('Название/идентификатор ноутбука: ' + img_anchor.laptop_name);
			}
			else{
				$('#defect-img-label').text('Название/идентификатор ноутбука: -');
			}
		}		
	}
}

/*
*
*	Load multiple images on click on button "Загрузить изображения из директории"
*
*/
$( "#load_imgs" ).on( "click", function() {
  	const inputElement = document.createElement('input');
	inputElement.type = 'file';
        inputElement.multiple = true;
        inputElement.accept = '.png,.jpg,.jpeg';
	inputElement.style.display = 'none'; 
	document.body.appendChild(inputElement);

	inputElement.click();

	inputElement.onchange = async (e) => {
    		const files = e.target.files;
		image_arr_tmp = [];
 
    		for (const file of files) {	
			var elem_list = document.getElementById("ss_elem_list")
			var elem = document.createElement('li')
			elem.id = 'ss_elem_' + unique_id;
			elem.role = 'option';
			elem.innerHTML = `<span class="checkmark" aria-hidden="true"></span>
` + file.name;
			elem.addEventListener("click", ss_elem_on_click, false);
			elem_list.appendChild(elem);
			
			image_arr_tmp.push(new Img_anchor(unique_id, file.name));
			unique_id += 1;
    		}
	};


	document.body.removeChild(inputElement);

	var laptop_name = document.getElementById("laptop-name");
	var laptop_descr = document.getElementById("laptop-description");
	$("#cover").fadeIn(100);
	$("#hidden-popup").show();
} );

/*
*
*	Unload .dotx document on click on button "Сформировать и выгрузить отчет"
*
*/
$( "#unload_res" ).on( "click", function() {
  	
} );

/*
*
*	Ок
*
*/
$( "#popup_ok" ).on( "click", function() {	
  	for (const img_anchor of image_arr_tmp) {
		img_anchor.laptop_name = $("#laptop-name").val();
		img_anchor.laptop_dscr = $("#laptop-description").val();
	}
	image_arr.push(...image_arr_tmp);

	$('#laptop-name').val('');
	$('#laptop-description').val('');
	$("#cover").fadeOut(100);
	$("#hidden-popup").hide();
} );

