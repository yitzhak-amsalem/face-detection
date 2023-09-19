from flask import Flask, request, jsonify
from flask_cors import CORS
from RequestModel import RequestModel
from ResponseModel import ResponseModel




@app.route('/upload-image', methods=['POST'])
def uploadImage(data=None):
    try:
        data = request.get_json()
        requestModel = RequestModel(**data)
        responseModel = ResponseModel(requestModel)
        filterImages = ResponseModel.process(responseModel)
        ResponseModel.deleteImages(responseModel)
        return jsonify({"result": filterImages})
    except Exception as e:
        return "error!!", e



# if __name__ == '__main__':
#     app.run()
